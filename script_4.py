
# Create App.css
app_css = '''* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  color: #eee;
  min-height: 100vh;
}

.App {
  min-height: 100vh;
}

nav {
  background: #0f3460;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav h1 {
  color: #e94560;
}

nav button {
  background: #e94560;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.auth-box {
  background: rgba(15, 52, 96, 0.8);
  padding: 40px;
  border-radius: 15px;
  width: 400px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.5);
}

.auth-box h2 {
  color: #e94560;
  margin-bottom: 30px;
  text-align: center;
}

.auth-box form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.auth-box input {
  padding: 12px;
  background: rgba(26, 26, 46, 0.8);
  border: 2px solid #0f3460;
  border-radius: 8px;
  color: #eee;
  font-size: 16px;
}

.auth-box button {
  background: #e94560;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}

.auth-box p {
  text-align: center;
  margin-top: 20px;
  color: #e94560;
  cursor: pointer;
}

.dashboard {
  padding: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 30px 0;
}

.stat-card {
  background: rgba(15, 52, 96, 0.5);
  padding: 25px;
  border-radius: 10px;
  border: 2px solid #e94560;
  text-align: center;
}

.stat-card h3 {
  color: #aaa;
  font-size: 14px;
  margin-bottom: 10px;
}

.stat-card p {
  font-size: 36px;
  color: #e94560;
  font-weight: bold;
}

.password-section {
  background: rgba(15, 52, 96, 0.5);
  padding: 25px;
  border-radius: 10px;
  margin-top: 30px;
}

.password-section button {
  background: #e94560;
  color: white;
  padding: 12px 30px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin-bottom: 20px;
}

.add-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.add-form input {
  flex: 1;
  padding: 10px;
  background: rgba(26, 26, 46, 0.8);
  border: 2px solid #0f3460;
  border-radius: 8px;
  color: #eee;
}

.add-form button {
  background: #4caf50;
  padding: 10px 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #0f3460;
}

th {
  background: #0f3460;
  font-weight: bold;
}

tr:hover {
  background: rgba(15, 52, 96, 0.3);
}

td button {
  background: #f44336;
  color: white;
  padding: 8px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}
'''

with open('privacy-dashboard-mern/frontend/src/App.css', 'w') as f:
    f.write(app_css)

# Create main README
main_readme = '''# Digital Privacy Dashboard - MERN Stack

A full-stack web application for managing passwords and digital privacy built with MongoDB, Express, React, and Node.js.

## 🚀 Features

- User Authentication (JWT)
- Password Generator
- Password Strength Analyzer  
- Encrypted Password Vault
- Security Activity Logs
- Dashboard Analytics
- Responsive Design

## 📦 Tech Stack

**Frontend:**
- React 18
- Axios
- Chart.js
- React Router

**Backend:**
- Node.js
- Express.js
- MongoDB with Mongoose
- JWT Authentication
- bcryptjs for password hashing

## 🛠️ Setup Instructions

### Backend Setup

1. Navigate to backend folder:
```bash
cd backend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```
PORT=5000
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
FRONTEND_URL=http://localhost:3000
```

4. Start backend server:
```bash
npm start
```

Backend runs on http://localhost:5000

### Frontend Setup

1. Navigate to frontend folder:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
```

4. Start React app:
```bash
npm start
```

Frontend runs on http://localhost:3000

## 🌐 Deployment

### Backend (Render/Railway/Heroku)

1. Push code to GitHub
2. Connect repository to hosting platform
3. Add environment variables
4. Deploy

### Frontend (Vercel/Netlify)

1. Push code to GitHub
2. Import project to Vercel/Netlify
3. Add REACT_APP_API_URL environment variable
4. Deploy

## 📝 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

### Passwords (Protected)
- `GET /api/passwords` - Get all passwords
- `POST /api/passwords` - Add new password
- `DELETE /api/passwords/:id` - Delete password

### Logs (Protected)
- `GET /api/logs` - Get security logs

## 👨‍💻 Developer

Your Name - VIT University

## 📄 License

MIT License
'''

with open('privacy-dashboard-mern/README.md', 'w') as f:
    f.write(main_readme)

print("✅ Frontend styling and README created")
print("   - src/App.css")
print("   - README.md")
