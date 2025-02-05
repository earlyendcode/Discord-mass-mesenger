# 🤖 Discord Mass Messenger

**Discord Mass Messenger** is a tool for sending bulk messages to friends on Discord with support for multiple accounts.

## ⚡ Features

- Automatic token loading from a file.
- Retrieving the friends list from each account.
- Sending messages with adjustable delay.
- Bypassing Discord limits (if possible).
- Logging the sending process.

## 🛠 Installation

Install dependencies:
   ```bash
   pip install requests colorama
   ```
Save tokens in the `token.txt` file (one per line).

Run the script:
   ```bash
   python xaxa.py
   ```

## 🔧 Usage

1. Run the script.
2. Enter the message text.
3. Specify the delay between messages (recommended 5-10 sec).
4. The script will start processing and send messages to all friends.

## 🖥 Example Output

```
========== ╚ Found X Tokens ╝ ==========
Enter spam message: Hi! How are you?
Enter delay between messages (in seconds, from 0.50 to 10): 7
Using token: XXXXXXXXXXXXXXXXX
Message successfully sent to user with ID 123456789012345678.
```

## ⚠ Important

- Using this script may violate Discord API rules.
- It is recommended to use **official Discord bots** for safe operation.
- The developer is not responsible for any consequences.

## 📜 License

This project is distributed under the MIT license. You are free to use and modify it.

