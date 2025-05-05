import React from 'react';

const OAuthButtons: React.FC = () => {
  const handleGitHubLogin = async () => {
    try {
      const res = await fetch('http://localhost:8000/auth/oauth/github');
      const data = await res.json();
      if (data.url) {
        window.location.href = data.url; // Redirect to GitHub login
      } else {
        console.error("GitHub login URL not received");
      }
    } catch (error) {
      console.error("GitHub OAuth error:", error);
    }
  };

  return (
    <div className="flex flex-col items-center mt-4 gap-2">
      <button
        onClick={handleGitHubLogin}
        className="bg-gray-800 text-white px-6 py-2 rounded hover:bg-gray-700"
      >
        Login with GitHub
      </button>
    </div>
  );
};

export default OAuthButtons;
