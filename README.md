# 🤖 Local AI Chatbot Projects (Ollama + Python)

This project demonstrates the development of local AI chatbot systems using Ollama and Python. It includes both terminal-based and programmable chatbot implementations, focusing on lightweight AI deployment and model evaluation.

## 📌 Projects Included

### 1. Ollama Terminal Chatbot
- Runs directly in terminal
- Uses TinyLlama model
- Command-based interaction

### 2. Python-Based Chatbot
- Built using Python
- Integrated with Ollama API
- Interactive chatbot loop

## ⚙️ Technologies Used
- Python
- Ollama
- TinyLlama
- Local LLMs

  ## 🧪 Model Testing

Both TinyLlama and Phi4 models were set up and tested using Ollama.

- ✅ TinyLlama: Used for the main chatbot due to low resource requirements
- 🚀 Phi4: Configured and tested; capable of running on higher-resource systems

This project demonstrates working with both lightweight and larger LLMs and selecting models based on system constraints.

## ⚖️ Model Comparison

| Model       | Status     | Performance | Requirement |
|------------|----------- |------------|-------------|
| TinyLlama  | Running ✅ | Fast       | Low RAM     |
| Phi4       | Running ✅ | High       | High RAM    |

## 🧠 Key Learnings

- Understanding local LLM deployment
- Managing hardware constraints in AI systems
- Comparing lightweight vs large AI models
- Integrating Ollama with Python

## 🚀 How to Run

### Terminal Chatbot
```bash
ollama run tinyllama
