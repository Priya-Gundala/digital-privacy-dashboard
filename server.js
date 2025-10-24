const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const app = express();

app.use(express.json());
app.use(cors({ origin: process.env.FRONTEND_URL || '*', credentials: true }));

mongoose.connect(process.env.MONGODB_URI)
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log('Error:', err));

const UserSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  username: { type: String, required: true },
  password: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

const PasswordSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  serviceName: { type: String, required: true },
  username: { type: String, required: true },
  password: { type: String, required: true },
  notes: String,
  strength: String,
  createdAt: { type: Date, default: Date.now }
});

const LogSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  action: { type: String, required: true },
  status: { type: String, default: 'success' },
  timestamp: { type: Date, default: Date.now }
});

const User = mongoose.model('User', UserSchema);
const Password = mongoose.model('Password', PasswordSchema);
const Log = mongoose.model('Log', LogSchema);

const auth = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.userId = user.id;
    next();
  });
};

app.post('/api/auth/register', async (req, res) => {
  try {
    const { email, username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ email, username, password: hashedPassword });
    await user.save();
    res.status(201).json({ message: 'User registered', user: { id: user._id, email, username } });
  } catch (error) {
    res.status(500).json({ error: 'Registration failed' });
  }
});

app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ email });
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });
    const isValid = await bcrypt.compare(password, user.password);
    if (!isValid) return res.status(401).json({ error: 'Invalid credentials' });
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '7d' });
    res.json({ token, user: { id: user._id, email: user.email, username: user.username } });
  } catch (error) {
    res.status(500).json({ error: 'Login failed' });
  }
});

app.get('/api/passwords', auth, async (req, res) => {
  const passwords = await Password.find({ userId: req.userId });
  res.json(passwords);
});

app.post('/api/passwords', auth, async (req, res) => {
  const newPassword = new Password({ ...req.body, userId: req.userId });
  await newPassword.save();
  res.status(201).json(newPassword);
});

app.delete('/api/passwords/:id', auth, async (req, res) => {
  await Password.findOneAndDelete({ _id: req.params.id, userId: req.userId });
  res.json({ message: 'Deleted' });
});

app.get('/api/logs', auth, async (req, res) => {
  const logs = await Log.find({ userId: req.userId }).sort({ timestamp: -1 });
  res.json(logs);
});

app.get('/', (req, res) => {
  res.json({ message: 'Privacy Dashboard API', version: '1.0.0' });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server on port ${PORT}`));
