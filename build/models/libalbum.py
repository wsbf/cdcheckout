import db

class LibalbumModel(db.DatabaseModel):
	''' Represents the table `libalbum`, which lists all albums with information
	about current rotation category, etc. ''' 
	
	def searchByRotation(self, rotationID):
		self.cursor.execute("""SELECT *
			FROM  `libalbum` ,  `libartist` 
			WHERE libalbum.rotationID =%s
			AND libalbum.artistID = libartist.artistID
			ORDER BY albumID DESC""", (rotationID,))
		result = self.cursor.fetchall()
		return result

	def searchByArtist(self, artist_name):
		#split words by whitespace
		words = artist_name.split() 
		# put wildcards between all words (and at begin/end)
		wildcardWords = "%" + "%".join(words) + "%"
		
		self.cursor.execute("""SElECT * FROM `libalbum`, `libartist` 
		WHERE libalbum.artistID = libartist.artistID 
		AND libartist.artist_name LIKE %s 
		ORDER BY (
		(CASE WHEN `artist_name` LIKE %s THEN 1 ELSE 0 END) + 
		(CASE WHEN `artist_name` LIKE %s THEN 1 ELSE 0 END)) DESC
		""", (wildcardWords,artist_name,wildcardWords,))
		result = self.cursor.fetchall()
		return result
	
	def searchByAlbumName(self, album_name):
		words = album_name.split()
		wildcardWords = "%" + "%".join(words) + "%"
		self.cursor.execute("""SELECT * FROM `libalbum`, `libartist`
			WHERE libalbum.artistID = libartist.artistID
			AND libalbum.album_name LIKE %s""", (wildcardWords,album_name,\
			wildcardWords))
		result = self.cursor.fetchall()
		return result
	
	def listAvailableToBeReviewed(self):
		''' Lists all albums marked as To Be Reviewed that are
			not already checked out'''
		self.cursor.execute("""
			SELECT libalbum.albumID, libalbum.album_name, libartist.artist_name
			FROM  `libalbum` ,  `libartist`
			WHERE libalbum.albumID NOT IN (SELECT albumID FROM check_out)
			AND libalbum.artistID = libartist.artistID 
			ORDER BY albumID DESC""")
		result = self.cursor.fetchall()
		return result
	
	
#	def search(self, searchString):
#		searchByArtist(searchString)
if __name__ == "__main__":
	l = LibalbumModel()
	list = l.searchByArtist("dr. dog")
	print list

