const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();
const PORT = 3000;

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index", { emotion: null, error: null });
});

app.post("/predict", async (req, res) => {
  const { sentence } = req.body;

  try {
    const response = await axios.post("http://127.0.0.1:8000/predict", {
      text: sentence
    });

    const emotion = response.data.emotion;
    res.render("index", { emotion, error: null });
  } catch (err) {
    res.render("index", { emotion: null, error: "Failed to get emotion." });
  }
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
