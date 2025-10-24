# Digital Privacy Dashboard - MERN Stack

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
