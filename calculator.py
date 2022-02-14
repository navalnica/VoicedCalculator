import os
import math
import winsound
import tkinter as tk


def play_wav_file(filepath):
	if os.path.isfile(filepath):
		print(f'playing "{filepath}"')
		winsound.PlaySound(filepath, winsound.SND_FILENAME)
	else:
		print(f'"{filepath}" does not exist')


class Calculator:

	def handle_exception(self, exception):
		self.text_field.delete(0, tk.END)
		print(exception)
		self.text_field.insert(0, 'Памылка')
		play_wav_file(os.path.join('voice', 'памылка.wav'))

	def voice_result(self):
		text_to_voice = self.expression
		text_to_voice = text_to_voice.split('.')
		# voice up to 3 digits after the period
		text_to_voice = text_to_voice[0] if len(text_to_voice) == 1 \
			else '.'.join([text_to_voice[0], text_to_voice[1][:3]])
		print(f'voice_result(). voicing text: "{text_to_voice}"')

		for char in text_to_voice:
			wav_file_name = self.button_name_2_wav_file_name.get(char, char)
			play_wav_file(os.path.join('voice', f'{wav_file_name}.wav'))

	def equals(self):
		play_wav_file(os.path.join('voice', 'падлік.wav'))

		try:
			self.value = eval(self.expression)
			self.text_field.delete(0, tk.END)
			self.text_field.insert(0, self.value)
			self.voice_result()
		except Exception as e:
			self.handle_exception(e)

		self.calculated = True

	def squareroot(self):
		play_wav_file(os.path.join('voice', 'корань.wav'))

		try:
			self.value = eval(self.expression)
			self.sqrtval = math.sqrt(self.value)
			self.text_field.delete(0, tk.END)
			self.text_field.insert(0, self.sqrtval)
			self.voice_result()
		except Exception as e:
			self.handle_exception(e)

		self.calculated = False

	def square(self):
		play_wav_file(os.path.join('voice', 'квадрат.wav'))

		try:
			self.value = eval(self.expression)
			self.sqval = self.value * self.value
			self.text_field.delete(0, tk.END)
			self.text_field.insert(0, self.sqval)
			self.voice_result()
		except Exception as e:
			self.handle_exception(e)

		self.calculated = False

	def clear_all(self):
		""" Clear the whole text input field. """

		play_wav_file(os.path.join('voice', 'ачысьціць.wav'))

		self.text_field.delete(0, tk.END)

		self.calculated = False

	def clear(self):
		""" Remove last symbol. """

		play_wav_file(os.path.join('voice', 'выдаліць.wav'))

		txt = self.text_field.get()[:-1]
		self.text_field.delete(0, tk.END)
		self.text_field.insert(0, txt)

		self.calculated = False

	def action(self, button_name):
		""" Pressed button's value is inserted into the end of the text area. """

		if self.calculated is True:
			# if digit is entered after last calculation - clear input field.
			# if operand is entered - allow new operation to use last calculations result.
			if isinstance(button_name, int) or button_name in '()':
				self.text_field.delete(0, tk.END)
			self.calculated = False

		wav_file_name = self.button_name_2_wav_file_name.get(button_name, button_name)
		play_wav_file(os.path.join('voice', f'{wav_file_name}.wav'))

		self.text_field.insert(tk.END, button_name)

	def _init_window_fields(self, master):
		self.text_field = tk.Entry(master)
		self.text_field.grid(row=0, column=0, columnspan=6, pady=10)
		self.text_field.focus_set()  # Sets focus on the input text area

		tk.Button(master, text="0", width=3, command=lambda: self.action(0)).grid(row=4, column=0, padx=5, pady=5)
		tk.Button(master, text="1", width=3, command=lambda: self.action(1)).grid(row=3, column=0, padx=5, pady=5)
		tk.Button(master, text="2", width=3, command=lambda: self.action(2)).grid(row=3, column=1, padx=5, pady=5)
		tk.Button(master, text="3", width=3, command=lambda: self.action(3)).grid(row=3, column=2, padx=5, pady=5)
		tk.Button(master, text="4", width=3, command=lambda: self.action(4)).grid(row=2, column=0, padx=5, pady=5)
		tk.Button(master, text="5", width=3, command=lambda: self.action(5)).grid(row=2, column=1, padx=5, pady=5)
		tk.Button(master, text="6", width=3, command=lambda: self.action(6)).grid(row=2, column=2, padx=5, pady=5)
		tk.Button(master, text="7", width=3, command=lambda: self.action(7)).grid(row=1, column=0, padx=5, pady=5)
		tk.Button(master, text="8", width=3, command=lambda: self.action(8)).grid(row=1, column=1, padx=5, pady=5)
		tk.Button(master, text="9", width=3, command=lambda: self.action(9)).grid(row=1, column=2, padx=5, pady=5)

		tk.Button(master, text="+", width=3, command=lambda: self.action('+')).grid(row=4, column=3, padx=5, pady=5)
		tk.Button(master, text="x", width=3, command=lambda: self.action('x')).grid(row=2, column=3, padx=5, pady=5)
		tk.Button(master, text="-", width=3, command=lambda: self.action('-')).grid(row=3, column=3, padx=5, pady=5)
		tk.Button(master, text="÷", width=3, command=lambda: self.action('÷')).grid(row=1, column=3, padx=5, pady=5)
		tk.Button(master, text="%", width=3, command=lambda: self.action('%')).grid(row=4, column=2, padx=5, pady=5)
		tk.Button(master, text=".", width=3, command=lambda: self.action('.')).grid(row=4, column=1, padx=5, pady=5)
		tk.Button(master, text="(", width=3, command=lambda: self.action('(')).grid(row=2, column=4, padx=5, pady=5)
		tk.Button(master, text=")", width=3, command=lambda: self.action(')')).grid(row=2, column=5, padx=5, pady=5)

		tk.Button(master, text="=", width=10, command=lambda: self.equals()).grid(row=4, column=4, columnspan=2)
		tk.Button(master, text='AC', width=3, command=lambda: self.clear_all()).grid(row=1, column=4, padx=5, pady=5)
		tk.Button(master, text='C', width=3, command=lambda: self.clear()).grid(row=1, column=5, padx=5, pady=5)
		tk.Button(master, text="√", width=3, command=lambda: self.squareroot()).grid(row=3, column=4, padx=5, pady=5)
		tk.Button(master, text="x²", width=3, command=lambda: self.square()).grid(row=3, column=5, padx=5, pady=5)

		# master.pack(fill=tk.Y)

	def __init__(self, master: tk.Tk):
		master.title('Калькулятар')
		master.geometry('250x200')
		self._init_window_fields(master)

		self.calculated = False

		self.button_name_2_wav_file_name = {
			'+': 'плюс',
			'-': 'мінус',
			'x': 'памножыць',
			'÷': 'падзяліць',
			'.': 'кропка',
			'%': 'рэшта',
			'(': 'левая_дужка',
			')': 'правая_дужка',
		}

	@property
	def expression(self):
		expression = self.text_field.get()
		expression = expression.replace('÷', '/')
		expression = expression.replace('x', '*')
		print(f'expression: "{expression}"')
		return expression


if __name__ == '__main__':
	root = tk.Tk()

	# instantiate calculator
	calculator = Calculator(root)

	root.mainloop()
