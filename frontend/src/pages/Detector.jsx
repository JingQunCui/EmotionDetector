import { useState } from 'react';
import axios from 'axios';

export default function EmotionDetectorPage() {
  const [sentence, setSentence] = useState('');
  const [emotion, setEmotion] = useState(null);

  const handlePredict = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        import.meta.env.VITE_BACKEND_URL + '/predict',
        { text: sentence }
      );
      setEmotion(response.data.emotion);
    } catch (err) {
      setEmotion('Error fetching emotion.');
    }
  };

  return (
    <div>
      <h2>Emotion Detector</h2>
      <form onSubmit={handlePredict}>
        <input
          type="text"
          placeholder="Type a sentence..."
          value={sentence}
          onChange={e => setSentence(e.target.value)}
          required
        />
        <button type="submit">Analyze</button>
      </form>
      {emotion && <p>Detected Emotion: {emotion}</p>}
    </div>
  );
}
