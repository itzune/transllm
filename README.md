## transllm: An AI-powered translator using Ollama LLMs

transllm is a project that allows you to translate text files using the Ollama LLMs. 🧠💬

**Installation:**

1. Clone the repository:
   ```bash
   git clone https://github.com/itzune/transllm.git
   cd transllm
   ```
2. Create a virtual environment (optional):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Usage:**

1. Create a TXT file containing one sentence per line that you want to translate. This file should be in the same directory as the script.
2. Run the `translate_txt.py` script:
   ```bash
   python translate_txt.py
   ```

**Examples:**

Input file (input.txt):

```
Kaixo mundua!
Zer moduz zaude?
Eskerrik asko.
```

Running the script:

```bash
python translate_txt.py
Hello world!
How are you?
Thank you.
```

**TODO**

- [ ] Set arguments for input file and output
- [ ] Set arguments for SYSTEM prompt
