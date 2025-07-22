# manapps-gen-password 🔐

A lightweight and flexible CLI tool for generating secure, random passwords using Python.

---

## ⚙️ Usage

After installation, run the command:

```bash
manpass [OPTIONS]
```

### Example:

```bash
manpass --length 16 --no-symbols --upper
```

---

## 🔧 Options

| Option                    | Description                                       | Default  |
|---------------------------|---------------------------------------------------|----------|
| `--length INTEGER`        | Set the length of the password                   | `12`     |
| `--symbols / --no-symbols`| Include special characters like @, #, !          | `True`   |
| `--digits / --no-digits`  | Include numeric digits (0–9)                     | `True`   |
| `--upper / --no-upper`    | Include uppercase letters (A–Z)                  | `True`   |

---

## 🛠 Requirements

- Python 3.10 or higher  
- [`click`](https://pypi.org/project/click/)

---

## 📦 Installation

Install directly via pip:

```bash
pip install manpass
```

Or from source (for development):

```bash
git clone http://github.com/AbodyPrmaga/manapps-gen-password.git
cd manapps-gen-password
pip install .
```

---

## 👨‍💻 Author

**Abdelrahman**  
Feel free to contribute or open issues to improve this project.

---

## 🪪 License

This project is licensed under the MIT License.
