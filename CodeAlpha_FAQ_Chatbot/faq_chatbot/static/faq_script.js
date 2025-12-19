const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(sender, text) {
  const wrapper = document.createElement("div");
  wrapper.className = "message " + sender;

  const bubble = document.createElement("div");
  bubble.className = "bubble";

  const label = document.createElement("span");
  label.className = "bubble-label";
  label.textContent = sender === "user" ? "You" : "Bot";

  const content = document.createElement("span");
  content.textContent = text;

  bubble.appendChild(label);
  bubble.appendChild(content);
  wrapper.appendChild(bubble);
  chatBox.appendChild(wrapper);

  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const msg = userInput.value.trim();
  if (!msg) return;

  addMessage("user", msg);
  userInput.value = "";
  userInput.focus();

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    addMessage("bot", data.response);
  } catch (err) {
    addMessage("bot", "Sorry, something went wrong. Please try again.");
  }
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keyup", function (e) {
  if (e.key === "Enter") sendMessage();
});
