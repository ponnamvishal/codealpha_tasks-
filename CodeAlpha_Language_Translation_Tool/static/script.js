const inputText = document.getElementById("input-text");
const outputText = document.getElementById("output-text");
const srcLang = document.getElementById("src-lang");
const destLang = document.getElementById("dest-lang");
const translateBtn = document.getElementById("translate-btn");
const copyBtn = document.getElementById("copy-btn");
const speakBtn = document.getElementById("speak-btn");

async function translateText() {
  const text = inputText.value.trim();
  if (!text) {
    outputText.value = "";
    return;
  }

  const payload = {
    text: text,
    src: srcLang.value,
    dest: destLang.value
  };

  try {
    const res = await fetch("/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    outputText.value = data.translated_text || "";
  } catch (err) {
    outputText.value = "Error while contacting server.";
  }
}

translateBtn.addEventListener("click", translateText);

inputText.addEventListener("keyup", (e) => {
  if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
    translateText();
  }
});

copyBtn.addEventListener("click", async () => {
  const text = outputText.value.trim();
  if (!text) return;
  try {
    await navigator.clipboard.writeText(text);
    copyBtn.textContent = "Copied!";
    setTimeout(() => (copyBtn.textContent = "Copy"), 1200);
  } catch (err) {
    alert("Copy not supported in this browser.");
  }
});

speakBtn.addEventListener("click", () => {
  const text = outputText.value.trim();
  if (!text) return;

  if (!("speechSynthesis" in window)) {
    alert("Text‑to‑speech not supported in this browser.");
    return;
  }

  const utterance = new SpeechSynthesisUtterance(text);

  const langMap = {
    English: "en",
    Hindi: "hi",
    Telugu: "te",
    Tamil: "ta",
    Kannada: "kn",
    Malayalam: "ml",
    Gujarati: "gu",
    Bengali: "bn",
    Spanish: "es",
    French: "fr",
    German: "de",
    Arabic: "ar",
    Japanese: "ja",
    Korean: "ko"
  };

  const targetName = destLang.value;
  const langCode = langMap[targetName] || "en";
  utterance.lang = langCode;

  const voices = window.speechSynthesis.getVoices();
  const match = voices.find(v => v.lang.toLowerCase().startsWith(langCode));
  if (match) {
    utterance.voice = match;
  }

  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utterance);
});
