import db

class MediumsModel(db.DatabaseModel):
	def list(self):
		self.cursor.execute("""SELECT * FROM def_mediums""")
		return self.cursor.fetchall()

if __name__ == "__main__":
	m = MediumsModel()
	print m.list()
