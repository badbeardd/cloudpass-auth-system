import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const AuthCallback: React.FC = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const verifyToken = async () => {
      const params = new URLSearchParams(window.location.search);
      const token = params.get('token');

      if (!token) {
        alert('Token missing from URL');
        return;
      }

      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/verify?token=${token}`);
        if (!response.ok) throw new Error('Token verification failed');

        const email = new URL(response.url).searchParams.get('email');
        if (email) {
          localStorage.setItem('userEmail', email);
          navigate('/dashboard');
        } else {
          alert('Invalid server response');
        }
      } catch (err) {
        console.error(err);
        alert('Login verification failed');
      }
    };

    verifyToken();
  }, [navigate]);

  return <p>Verifying login...</p>;
};

export default AuthCallback;
