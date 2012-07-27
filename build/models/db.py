import MySQLdb

class DatabaseModel(object):
	# making this a static variable ensures that only one connection is used
	conn = None
	def __init__(self):
		if not DatabaseModel.conn:
			DatabaseModel.conn = MySQLdb.connect(host="new.wsbf.net", \
				user="cdcheckout", passwd="Jtj5MABzJcm2vtuh", db="wsbf", charset="utf8", use_unicode=True)
			DatabaseModel.conn.autocommit(True)
		self.cursor = DatabaseModel.conn.cursor()#MySQLdb.cursors.DictCursor)
