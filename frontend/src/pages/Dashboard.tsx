import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Dashboard: React.FC = () => {
  const [email, setEmail] = useState<string | null>(null);
  const navigate = useNavigate();

  // ✅ Store email and token from URL (first-time login)
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const emailFromURL = params.get('email');
    const tokenFromURL = params.get('token');
    if (emailFromURL) {
      localStorage.setItem('userEmail', emailFromURL);
    }
    if (tokenFromURL) {
      localStorage.setItem('token', tokenFromURL);
    }
  }, []);

  // ✅ Load email and check login status
  useEffect(() => {
    const storedEmail = localStorage.getItem('userEmail');
    if (!storedEmail) {
      navigate('/');
    } else {
      setEmail(storedEmail);
    }

    // ✅ Try calling protected API
    const token = localStorage.getItem('token');
    if (token) {
      fetch('http://localhost:8000/user/profile', {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then(res => res.json())
        .then(data => console.log("🔐 Protected API response:", data))
        .catch(err => console.error("❌ API error:", err));
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('userEmail');
    localStorage.removeItem('token');
    navigate('/');
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-4">
      <h1 className="text-2xl font-bold">Welcome to Dashboard</h1>
      <p className="text-lg">Logged in as: {email}</p>
      <button
        className="bg-red-500 text-white px-4 py-2 rounded"
        onClick={handleLogout}
      >
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
