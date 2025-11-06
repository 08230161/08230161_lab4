from typing import TYPE_CHECKING

if TYPE_CHECKING:
	import pymysql  # type: ignore

try:
	import pymysql  # type: ignore
	pymysql.install_as_MySQLdb()
except Exception:
	# If pymysql isn't installed at runtime, skip installation;
	# an alternative MySQLdb implementation may be available instead.
	pass
