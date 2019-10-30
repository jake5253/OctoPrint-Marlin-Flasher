from .arduino_flasher import ArduinoFlasher
from .platformio_flasher import PlatformIOFlasher
from .unsupported_flasher import UnsupportedFlasher
from .platform_type import PlatformType


class MarlinFlasher:

	def __init__(self, settings, printer):
		self.__firmware = None
		self.__settings = settings
		self.__arduino_flasher = ArduinoFlasher(settings, printer)
		self.__platformio_flasher = PlatformIOFlasher(settings, printer)
		self.__unsupported_flasher = UnsupportedFlasher(settings, printer)

	def __get_implementation(self):
		platform = self.__settings.get_platform_type()
		if platform == PlatformType.ARDUINO:
			return self.__arduino_flasher
		elif platform == PlatformType.PLATFORM_IO:
			return self.__platformio_flasher
		else:
			return self.__unsupported_flasher

	@staticmethod
	def __run_after_checks(impl, func):
		errors = impl.do_checks()
		if errors:
			return errors
		return func()

	def upload_file(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.upload_file)

	def core_search(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.core_search)

	def lib_search(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.lib_search)

	def core_install(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.core_install)

	def lib_install(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.lib_install)

	def core_uninstall(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.core_uninstall)

	def lib_uninstall(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.lib_uninstall)

	def board_listall(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.board_listall)

	def board_details(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.board_details)

	def compile(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.compile)

	def upload(self):
		impl = self.__get_implementation()
		self.__run_after_checks(impl, impl.upload)

