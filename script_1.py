
# Create all backend files
backend_files = {
    'server.js': '''const express = require('express');
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
''',
    
    'package.json': '''{
  "name": "privacy-dashboard-backend",
  "version": "1.0.0",
  "description": "Digital Privacy Dashboard Backend",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^8.0.0",
    "bcryptjs": "^2.4.3",
    "jsonwebtoken": "^9.0.2",
    "dotenv": "^16.3.1",
    "cors": "^2.8.5"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}''',
    
    '.env.example': '''PORT=5000
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/privacy_dashboard
JWT_SECRET=your_secret_key_here
JWT_EXPIRE=7d
NODE_ENV=production
FRONTEND_URL=http://localhost:3000
''',
    
    '.gitignore': '''node_modules/
.env
*.log
.DS_Store
''',
    
    'README.md': '''# Digital Privacy Dashboard - Backend

## Setup
1. npm install
2. Create .env file (copy from .env.example)
3. Add your MongoDB URI
4. npm start

## API Endpoints
- POST /api/auth/register
- POST /api/auth/login
- GET /api/passwords (protected)
- POST /api/passwords (protected)
- DELETE /api/passwords/:id (protected)
- GET /api/logs (protected)

## Deployment
Deploy to Render, Railway, or Heroku
'''
}

# Write backend files
for filename, content in backend_files.items():
    with open(f'privacy-dashboard-mern/backend/{filename}', 'w') as f:
        f.write(content)

print("✅ Backend files created")
print("   - server.js")
print("   - package.json")
print("   - .env.example")
print("   - .gitignore")
print("   - README.md")
