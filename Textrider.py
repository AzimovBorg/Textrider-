import pyttsx3


engine = pyttsx3.init()     # инициализация движка
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
# зададим свойства
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

text_file = open("test.txt", "r", encoding= "utf-8"  )
data = text_file.read()
engine.say(data)# запись фразы в очередь
text_file.close()

# очистка очереди и воспроизведение текста
engine.runAndWait()

# выполнение кода останавливается, пока весь текст не сказан

"""
Простейший код, который сохраняет текст на русском в аудиофайл:
from gtts import gTTS

tts = gTTS('И это тоже интересно!', lang='ru')
tts.save('sound_ru.mp3')
tts = gTTS("It's amazing!", lang='en')
tts.save('sound_en.mp3')
"""
"""
# Получить список доступных голосов можно так:
engine = pyttsx3.init()    # Инициализировать голосовой движок.
voices = engine.getProperty('voices')

for voice in voices:    # голоса и параметры каждого
    print('------')
    print(f'Имя: {voice.name}')
    print(f'ID: {voice.id}')
    print(f'Язык(и): {voice.languages}')
    print(f'Пол: {voice.gender}')
    print(f'Возраст: {voice.age}')"""

# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0