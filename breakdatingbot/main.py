from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram import Bot, types
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

from breakdb import breakdb

from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=logging.INFO)
breakdatingkey = os.getenv('BREAKDATINGKEY')
bot = Bot(breakdatingkey)

logging.basicConfig(level=logging.INFO)

db = breakdb('break.db')

#хендлер команды /start
@dp.message_handler(commands=['start'],state='*')
async def start(message:types.Message):

	#кнопки для волшебного входа

	start_button = KeyboardButton("Hello, let's break together")

	break_start = ReplyKeyboardMarkup(one_time_keyboard=True)

	break_start.add(start_button)
	await message.answer("Hello\n\n,reply_markup=break_start")
	if(not db.user_exists(message.from_user.id)):
		#если юзера нет в базе добавляем его
		db.add_user(message.from_user.username,message.from_user.id,message.from_user.full_name)
		await bot.send_message(-1001406772763,f'New User!\nID - {str(message.from_user.id)}\nusername - {str(message.from_user.username)}')

		# хендлер для команды Зайти в волшебный мир

@ dp.message_handler(
	lambda message: message.text == 'Welcome home' or message.text == '/menu_break',
		state='*')

def menu_break(message: types.Message):
	'''Функция для меню самого бота'''
	# кнопки меню
	button_search = KeyboardButton('Find Somebody')

	button_create_profile = KeyboardButton('Create a profile')

	button_edit_profile = KeyboardButton('Edit profile')

	button_remove_profile = KeyboardButton('Delete')

	button_admin = KeyboardButton('Админка⚙️')

	menu = ReplyKeyboardMarkup()



#хендлер для создания анкеты

class CreateProfile(StatesGroup):
	name = State()
	description = State()
	city = State()
	photo = State()
	sex = State()
	age = State()
	social_link	 = State()


#хендлер старта для создания анкеты
@dp.message_handler(lambda message: message.text == 'Create profile',state='*')
async def create_profile(message : types.Message):
	#кнопки отмены
	button_exit = KeyboardButton('Exit')

	menu_exit = ReplyKeyboardMarkup()

	menu_exit.add(button_exit)

	if message.from_user.username != None:
		if(not db.profile_exists(message.from_user.id)):
			await message.answer("To create a profile you should give me some information about you\nLet's start with your name?",reply_markup=menu_exit)
			await CreateProfile.name.set()
		elif(db.profile_exists(message.from_user.id)) :
			await message.answer('You already have profile\n\n')
	else:
		await message.answer('Your telegram username is not filled!\n\nPlease do this to get \n Please go to the settings and change that')
#хендлер для заполнения имя
@dp.message_handler(state=CreateProfile.name)
async def create_profile_name(message: types.Message, state: FSMContext):
	if str(message.text) == 'Exit':
		await state.finish()
		await menu_break(message)
		return
	if len(str(message.text)) < 35 and (not str(message.text) in cus_ans.ban_symvols):
		await state.update_data(profile_name=message.text.lower())
		await message.reply(message.text.title() + 'Good for you, .name, what is your message to the world?')
		await CreateProfile.next()
	elif str(message.text) in cus_ans.ban_symvols:
		await message.answer('Forbidden symbols error')
	else:
		await message.answer(cus_ans.random_reapeat_list())
		#прерывание функции
		return

#хендлер для заполнение описания

@dp.message_handler(state=CreateProfile.description)
async def create_profile_description(message: types.Message, state: FSMContext):
	if str(message.text) == 'Exit':
		await state.finish()
		await menu_break(message)
		return
	if len(message.text) < 35 and (not str(message.text) in cus_ans.ban_symvols):
		await state.update_data(profile_description=message.text)
		await message.answer('Choose the city')
		await CreateProfile.next()
	elif str(message.text) in cus_ans.ban_symvols:
		await message.answer('Forbidden symbols error')
	else:
		await message.answer(cus_ans.random_reapeat_list())
		#прерывание функции
		return
#хендлер для заполнения города
@dp.message_handler(state=CreateProfile.city)
async def create_profile_city(message: types.Message, state: FSMContext):
	if str(message.text) == 'Exit':
		await state.finish()
		await menu_break(message)
		return
	if len(message.text) < 35 and (not str(message.text) in cus_ans.ban_symvols):
		await state.update_data(profile_city=message.text.lower())
		await message.answer('Прелестно, теперь добавим фотокарточку, что бы все знали какая ты красавица(хихи)🖼\n\nВажно отправлять фотографией, а не файлом!')
		await CreateProfile.next()
	elif str(message.text) in cus_ans.ban_symvols:
		await message.answer('Forbidden symbols error')
	else:
		await message.answer(cus_ans.random_reapeat_list())
		#прерывание функции
		return
#хендлер для заполнения фотографии
@dp.message_handler(state=CreateProfile.photo,content_types=['photo'])
async def create_profile_photo(message: types.Message, state: FSMContext):
	if str(message.text) == 'Exit':
		await state.finish()
		await menu_break(message)

	#кнопки выбора пола
	button_male = KeyboardButton('Male')

	button_wooman = KeyboardButton('Female')


	sex_input = ReplyKeyboardMarkup(one_time_keyboard=True)
	sex_input.add(button_male,button_wooman)

	await message.photo[-1].download('photo_user/' + str(message.from_user.id) + '.jpg')
	await message.answer('You look amazing',reply_markup=sex_input)
	await CreateProfile.next()
#хендлер для заполнения пола
@dp.message_handler(state=CreateProfile.sex)
async def create_profile_sex(message: types.Message, state: FSMContext):
	if str(message.text) == 'Exit':
		await state.finish()
		await menu_break(message)
		return
	if message.text == 'Мужчина' or message.text == 'Женщина':
		await state.update_data(profile_sex=message.text.lower())
		await message.answer('Amazing!\ntell me your age now\n')
		await CreateProfile.next()
		#прерывание функции
		return
	else:
		await message.answer(cus_ans.random_reapeat_list())
		#прерывание функции
		return

#хендлер для заполнения возвраста
@dp.message_handler(state=CreateProfile.age)
async def create_profile_age(message: types.Message, state: FSMContext):
	try:
		if str(message.text) == 'Exit':
			await state.finish()
			await menu_break(message)
			return
		if int(message.text) < 14:
			await message.answer("You're not old enough...")
			await message.answer(cus_ans.random_reapeat_list())

			#прерывание функции
			return
		elif int(message.text) > 6 and int(message.text) < 54:
			await state.update_data(profile_age=message.text)
			#кнопки меню
			button_skip = KeyboardButton('Skip')

			skip_input = ReplyKeyboardMarkup(one_time_keyboard=True)
			skip_input.add(button_skip)

			await CreateProfile.next()
		else:
			await answer.message('Only numbers')
			return
	except:
		await message.answer(cus_ans.random_reapeat_list())
		#прерывание функции
		return

#хендлер для удаления анкеты
@dp.message_handler(lambda message: message.text == 'Delete Profile')
async def delete_profile(message : types.Message):
	'''Функция для удаления анкеты'''

	try:
		db.delete_profile(message.from_user.id)
		await message.answer('Profile deleted successfully!')
		await menu_break(message)
	except:
		await message.answer(cus_ans.random_reapeat_list())
		return

#хендлер для редактирования анкеты
@dp.message_handler(lambda message: message.text == 'Change Profilee')
async def edit_profile(message : types.Message):
	'''Функция для меню редактирования анкеты'''
	try:
		if(not db.profile_exists(message.from_user.id)):
			await message.answer("You don't have a profile")
		elif(db.profile_exists(message.from_user.id)) :
			photo = open('photo_user/' + str(message.from_user.id) + '.jpg','rb')
			#кнопки выбора пола
			button_again = KeyboardButton('Fill your profile again')

			button_edit_description = KeyboardButton('Change about yourself')

			button_edit_age = KeyboardButton('Change your age')

			button_cancel = KeyboardButton('Exit')

			edit_profile = ReplyKeyboardMarkup(one_time_keyboard=True)
			edit_profile.add(button_again,button_edit_description,button_edit_age,button_cancel)
			caption = 'Your Profile:\n\nName - ' + str(db.all_profile(str(message.from_user.id))[0][3]).title() + '\nAbout you - ' + str(db.all_profile(str(message.from_user.id))[0][4]) + '\nCity - ' + str(db.all_profile(str(message.from_user.id))[0][5]).title() + '\nAge?) - ' + str(db.all_profile(str(message.from_user.id))[0][8])
			await message.answer_photo(photo,caption=caption,reply_markup=edit_profile)
			photo.close()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return

#хендлер для заполнения анкеты заново
@dp.message_handler(lambda message: message.text == 'Fill your profile again')
async def edit_profile_again(message : types.Message):
	'''Функция для заполнения анкеты заново'''
	try:
		db.delete_profile(message.from_user.id)
		await create_profile(message)

	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return

#класс машины состояний FSM
class EditProfile(StatesGroup):
	description_edit = State()
	age_edit = State()

#хендлеры для изменение возвраста и описания анкеты

@dp.message_handler(lambda message: message.text == 'Change your age' or message.text == 'Change about yourself')
async def edit_profile_age(message : types.Message):
	try:
		#кнопки для отмены
		button_cancel = KeyboardButton('Deny')

		button_cancel_menu = ReplyKeyboardMarkup(one_time_keyboard=True)

		button_cancel_menu.add(button_cancel)

		if message.text == 'Change age':
			await message.answer('How old are you?',reply_markup=button_cancel_menu)
			await EditProfile.age_edit.set()
		elif message.text == "What's your message to the world?":
			await message.answer('Change about yourself!',reply_markup=button_cancel_menu)
			await EditProfile.description_edit.set()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return
@dp.message_handler(state=EditProfile.age_edit)
async def edit_profile_age_step2(message: types.Message, state: FSMContext):
	'''Функция для обновления возвраста в бд'''
	try:
		if str(message.text) == 'Deny':
			await state.finish()
			await menu_break(message)

			return

		elif int(message.text) > 6 and int(message.text) < 54:
			await message.answer('Age successfully changed!')
			await state.update_data(edit_profile_age=message.text)
			user_data = await state.get_data()

			db.edit_age(user_data['edit_profile_age'],str(message.from_user.id))
			await state.finish()
			await edit_profile(message)
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		photoprint(e)
		return
@dp.message_handler(state=EditProfile.description_edit)
async def edit_profile_description(message: types.Message, state: FSMContext):
	'''Функция для обновления описания в бд'''
	try:
		if str(message.text) == 'Deny':
			await state.finish()
			await menu_break(message)

			return
		await message.answer('Description changed!')
		await state.update_data(edit_profile_description=message.text)
		user_data = await state.get_data()

		db.edit_description(user_data['edit_profile_description'],str(message.from_user.id))
		await state.finish()
		await edit_profile(message)
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		print(e)
		return

@dp.message_handler(lambda message: message.text == 'Exit')
async def exit(message : types.Message):
	await menu_break(message)



#класс машины состояний FSM
class SearchProfile(StatesGroup):
	city_search = State()
	in_doing = State()

#хендлеры для поиска по анкетам
@dp.message_handler(lambda message: message.text == 'Find somebody for me!')
async def search_profile(message : types.Message):
	'''Функция для ввода пользователя своего города,последующей записи в бд'''
	try:
		if db.profile_exists(message.from_user.id) == False:
			await message.answer("You don't have a Profile, come back later!")
		else:
			await message.answer('Choose the city')
			await SearchProfile.city_search.set()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		await State.finish()
		print(e)
		return

@dp.message_handler(state=SearchProfile.city_search)
async def seach_profile_step2(message: types.Message, state: FSMContext):
	'''Функция поиска анкет после отправки пользователя своего города'''
	try:
		await state.update_data(search_profile_city=message.text.lower())

		user_data = await state.get_data()

		db.set_city_search(str(user_data['search_profile_city']),str(message.from_user.id))
		if (bool(len(db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))))):
			try:
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except:
				db.edit_zero_profile_status(message.from_user.id)
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			await state.update_data(last_profile_id=profile_id)
			db.edit_profile_status(str(message.from_user.id),db.search_profile_status(str(message.from_user.id))[0])

			#кнопки для оценки
			button_like = KeyboardButton('👍')

			button_dislike = KeyboardButton('👎')

			mark_menu = ReplyKeyboardMarkup()

			mark_menu.add(button_dislike,button_like)

			name_profile = str(db.get_info(profile_id)[3])
			age_profile = str(db.get_info(profile_id)[8])
			description_profile = str(db.get_info(profile_id)[4])
			social_link_profile = str(db.get_info(profile_id)[9])
			photo_profile = open('photo_user/' + str(profile_id) + '.jpg','rb')

			city = str(db.get_info_user(message.from_user.id)[6]).title()

			final_text_profile = f'Found somebody for you\n\n{name_profile},{age_profile},{city}\n{description_profile}'

			await message.answer_photo(photo_profile,caption=final_text_profile,reply_markup=mark_menu)


			await SearchProfile.next()
		else:
			await message.answer('No one from there')
			await state.finish()
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		await state.finish()
		await menu_break(message)
		print(e)

@dp.message_handler(state=SearchProfile.in_doing)
async def seach_profile_step3(message: types.Message, state: FSMContext):
	'''Функция поиска анкет после отправки пользователя своей оценки(лайк,дизлайк,репорт)'''
	try:
		if str(message.text) == '👍':
			if str(message.text) == '/start' or str(message.text) == 'Exit':
				await state.finish()
				await menu_break(message)

			user_data = await state.get_data()

			try:
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except IndexError:
				db.edit_zero_profile_status(message.from_user.id)
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except Exception as e:
				print(e)
				await state.finish()
				await menu_break(message)
			await state.update_data(last_profile_id=profile_id)
			if db.add_like_exists(str(message.from_user.id),user_data['last_profile_id']) == False:
				db.add_like(str(message.from_user.id),user_data['last_profile_id'])
				db.up_rating(db.check_rating(profile_id)[0],user_data['last_profile_id'])
			db.edit_profile_status(str(message.from_user.id),db.search_profile_status(str(message.from_user.id))[0])
			name_profile = str(db.get_info(profile_id)[3])
			age_profile = str(db.get_info(profile_id)[8])
			description_profile = str(db.get_info(profile_id)[4])
			social_link_profile = str(db.get_info(profile_id)[9])
			photo_profile = open('photo_user/' + str(profile_id) + '.jpg','rb')

			city = str(user_data['search_profile_city']).title()

			final_text_profile = f'Found somebody for you️\n\n{name_profile},{age_profile},{city}\n{description_profile}'

			await message.answer_photo(photo_profile,caption=final_text_profile)

			name_profile_self = str(db.get_info(str(message.from_user.id))[3])
			age_profile_self = str(db.get_info(str(message.from_user.id))[8])
			description_profile_self = str(db.get_info(str(message.from_user.id))[4])
			social_link_profile_self = str(db.get_info(str(message.from_user.id))[9])
			photo_profile_self = open('photo_user/' + str(message.from_user.id) + '.jpg','rb')

			final_text_profile_self = f'Somebody want to get along with you..\n\n{name_profile_self},{age_profile_self},{city}\n{description_profile_self}\n\nЧего ты ждёшь,беги знакомиться - @{str(message.from_user.username)}'

			await bot.send_photo(user_data['last_profile_id'],photo_profile_self,caption=final_text_profile_self)


			return
			await state.finish()
		elif str(message.text) == '👎':
			if str(message.text) == '/start' or str(message.text) == 'Exit':
				await state.finish()
				await menu_break(message)

			user_data = await state.get_data()

			try:
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except IndexError:
				db.edit_zero_profile_status(message.from_user.id)
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except Exception as e:
				print(e)
				await state.finish()
				await menu_break(message)

			await state.update_data(last_profile_id=profile_id)

			db.edit_profile_status(str(message.from_user.id),db.search_profile_status(str(message.from_user.id))[0])
			name_profile = str(db.get_info(profile_id)[3])
			age_profile = str(db.get_info(profile_id)[8])
			description_profile = str(db.get_info(profile_id)[4])
			social_link_profile = str(db.get_info(profile_id)[9])
			photo_profile = open('photo_user/' + str(profile_id) + '.jpg','rb')

			city = str(user_data['search_profile_city']).title()

			final_text_profile = f'Found somebody for you️️\n\n{name_profile},{age_profile},{city}\n{description_profile}'

			await message.answer_photo(photo_profile,caption=final_text_profile)

			if str(message.text) == '/start' or str(message.text) == 'Exit':
				await state.finish()
				await menu_break(message)

			user_data = await state.get_data()



			try:
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except IndexError:
				db.edit_zero_profile_status(message.from_user.id)
				profile_id = db.search_profile(str(db.get_info_user(str(message.from_user.id))[6]),str(db.get_info(str(message.from_user.id))[8]),str(db.get_info(str(message.from_user.id))[7]))[db.search_profile_status(str(message.from_user.id))[0]][0]
			except Exception as e:
				print(e)
				await state.finish()
				await menu_break(message)

			name_profile = str(db.get_info(profile_id)[3])
			age_profile = str(db.get_info(profile_id)[8])
			description_profile = str(db.get_info(profile_id)[4])
			social_link_profile = str(db.get_info(profile_id)[9])
			photo_profile = open('photo_user/' + str(profile_id) + '.jpg','rb')

			city = str(user_data['search_profile_city']).title()

			final_text_profile = f'Found somebody for you️️\n\n{name_profile},{age_profile},{city}\n{description_profile}'

			await message.answer_photo(photo_profile,caption=final_text_profile)
		else:
			await state.finish()
			await menu_break(message)
	except Exception as e:
		await message.answer(cus_ans.random_reapeat_list())
		await state.finish()
		await menu_break(message)
		print(e)
		return
