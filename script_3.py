
# Create main App.js for React
app_js = '''import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [user, setUser] = useState(null);
  const [view, setView] = useState('login');
  const [passwords, setPasswords] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setUser(JSON.parse(localStorage.getItem('user')));
      loadPasswords();
    }
  }, []);

  const loadPasswords = async () => {
    const token = localStorage.getItem('token');
    const res = await axios.get(`${API_URL}/api/passwords`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    setPasswords(res.data);
  };

  const login = async (email, password) => {
    const res = await axios.post(`${API_URL}/api/auth/login`, { email, password });
    localStorage.setItem('token', res.data.token);
    localStorage.setItem('user', JSON.stringify(res.data.user));
    setUser(res.data.user);
    loadPasswords();
  };

  const register = async (email, username, password) => {
    await axios.post(`${API_URL}/api/auth/register`, { email, username, password });
    alert('Registered! Please login.');
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
    setPasswords([]);
    setView('login');
  };

  if (!user) {
    return <AuthPage onLogin={login} onRegister={register} view={view} setView={setView} />;
  }

  return (
    <div className="App">
      <nav>
        <h1>Privacy Dashboard</h1>
        <button onClick={logout}>Logout</button>
      </nav>
      <Dashboard user={user} passwords={passwords} loadPasswords={loadPasswords} />
    </div>
  );
}

function AuthPage({ onLogin, onRegister, view, setView }) {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (view === 'login') {
      onLogin(email, password);
    } else {
      onRegister(email, username, password);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <h2>{view === 'login' ? 'Login' : 'Register'}</h2>
        <form onSubmit={handleSubmit}>
          <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          {view === 'register' && <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />}
          <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <button type="submit">{view === 'login' ? 'Login' : 'Register'}</button>
        </form>
        <p onClick={() => setView(view === 'login' ? 'register' : 'login')}>
          {view === 'login' ? 'Create account' : 'Already have account?'}
        </p>
      </div>
    </div>
  );
}

function Dashboard({ user, passwords, loadPasswords }) {
  return (
    <div className="dashboard">
      <h2>Welcome, {user.username}!</h2>
      <div className="stats">
        <div className="stat-card">
          <h3>Total Passwords</h3>
          <p>{passwords.length}</p>
        </div>
      </div>
      <PasswordList passwords={passwords} loadPasswords={loadPasswords} />
    </div>
  );
}

function PasswordList({ passwords, loadPasswords }) {
  const [showAdd, setShowAdd] = useState(false);

  return (
    <div className="password-section">
      <button onClick={() => setShowAdd(!showAdd)}>Add Password</button>
      {showAdd && <AddPasswordForm loadPasswords={loadPasswords} setShowAdd={setShowAdd} />}
      <table>
        <thead>
          <tr>
            <th>Service</th>
            <th>Username</th>
            <th>Password</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {passwords.map(pwd => (
            <tr key={pwd._id}>
              <td>{pwd.serviceName}</td>
              <td>{pwd.username}</td>
              <td>••••••••</td>
              <td><button>Delete</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function AddPasswordForm({ loadPasswords, setShowAdd }) {
  const [service, setService] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    await axios.post(`${API_URL}/api/passwords`, 
      { serviceName: service, username, password, strength: 'Strong' },
      { headers: { Authorization: `Bearer ${token}` }}
    );
    loadPasswords();
    setShowAdd(false);
  };

  return (
    <form onSubmit={handleSubmit} className="add-form">
      <input type="text" placeholder="Service" value={service} onChange={(e) => setService(e.target.value)} required />
      <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      <button type="submit">Save</button>
    </form>
  );
}

export default App;
'''

with open('privacy-dashboard-mern/frontend/src/App.js', 'w') as f:
    f.write(app_js)

# Create index.js
index_js = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
'''

with open('privacy-dashboard-mern/frontend/src/index.js', 'w') as f:
    f.write(index_js)

print("✅ React components created")
print("   - src/App.js")
print("   - src/index.js")
