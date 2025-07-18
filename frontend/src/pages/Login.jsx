// src/components/Login.jsx
import { useState } from "react";
import "../styles/global.css";


export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    // Add login logic here
    alert(`Logging in with ${username}`);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="w-full max-w-sm bg-white p-8 border border-gray-300 rounded-md shadow-md">
        <h1 className="text-3xl font-semibold text-center mb-6 font-sans">Instagram</h1>
        <form onSubmit={handleLogin} className="space-y-4">
          <input
            type="text"
            placeholder="Username"
            className="w-full px-4 py-2 border rounded bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full px-4 py-2 border rounded bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button
            type="submit"
            className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded font-semibold"
          >
            Log In
          </button>
        </form>

        <div className="flex justify-center my-4">
          <span className="text-gray-400 text-sm">OR</span>
        </div>

        <p className="text-center text-sm text-blue-500 hover:underline cursor-pointer">
          Forgot password?
        </p>
      </div>
    </div>
  );
}
