{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8472f36",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "def generate_password(length):\n",
    "    # Define the characters to use for generating the password\n",
    "    characters = string.ascii_letters + string.digits + string.punctuation\n",
    "\n",
    "    # Use random.choice to generate a password of the specified length\n",
    "    password = ''.join(random.choice(characters) for _ in range(length))\n",
    "\n",
    "    return password\n",
    "\n",
    "def main():\n",
    "    try:\n",
    "        # Prompt the user to specify the desired length of the password\n",
    "        password_length = int(input(\"Enter the desired password length: \"))\n",
    "\n",
    "        # Check if the specified length is valid\n",
    "        if password_length <= 0:\n",
    "            print(\"Invalid password length. Please enter a positive integer.\")\n",
    "        else:\n",
    "            # Generate and display the password\n",
    "            password = generate_password(password_length)\n",
    "            print(\"Generated Password:\", password)\n",
    "    except ValueError:\n",
    "        print(\"Invalid input. Please enter a valid integer for password length.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "940bade7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
