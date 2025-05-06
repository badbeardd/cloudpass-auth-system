import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL;

// 🔹 Send magic link to user's email
export const sendMagicLink = async (email: string) => {
  try {
    const res = await axios.post(`${API_BASE}/auth/magic-link`, {
      email,
    });
    return res.data;
  } catch (error) {
    console.error("Magic link error:", error);
    throw error;
  }
};

// 🔹 Handle magic link login (token verification)
export const verifyMagicLink = async (token: string) => {
  try {
    const res = await axios.post(`${API_BASE}/auth/verify`, {
      token,
    });
    return res.data;
  } catch (error) {
    console.error("Verification error:", error);
    throw error;
  }
};

// 🔹 Get user profile (secured route)
export const getUserProfile = async (token: string) => {
  try {
    const res = await axios.get(`${API_BASE}/user/profile`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return res.data;
  } catch (error) {
    console.error("Profile fetch error:", error);
    throw error;
  }
};
