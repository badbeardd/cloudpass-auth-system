import { useState } from 'react';
import axios from 'axios';
import OAuthButtons from '../components/OAuthButtons';

const Home = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSendLink = async () => {
    console.log("Send button clicked");

    try {
      const res = await axios.post(
        `${import.meta.env.VITE_API_URL}/auth/magic-link`,
        { email }
      );
      console.log("Magic link sent:", res.data);
      setMessage('✅ Magic link sent! Check your inbox.');
    } catch (err: any) {
      console.error("Error sending magic link:", err);
      setMessage('❌ Failed to send magic link.');
    } finally {
      console.log("Request finished");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center gap-4">
      <h1 className="text-3xl font-bold">CloudPass Login</h1>

      <input
        type="email"
        placeholder="Enter your email"
        className="border p-2 rounded w-64"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <button
        onClick={handleSendLink}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Send Magic Link
      </button>

      <OAuthButtons />

      {message && <p className="text-sm mt-2">{message}</p>}
    </div>
  );
};

export default Home;
