def create_youtube_video(title,description) :
	newvideo = {"title" : title,"description" : description,"likes" : 0,"dislikes" : 0,"comments" : {}}
	return newvideo

def like (youtube_vid):
	if "likes" in youtube_vid:
		youtube_vid["likes"] = youtube_vid["likes"] +1

	return youtube_vid

def dislike (youtube_vid):
	if "dislikes" in youtube_vid:
		youtube_vid["dislikes"] = youtube_vid["dislikes"] +1

	return youtube_vid

def add_coment(youtubevideo,username,comment_text):
	 youtubevideo["comments"][username] = comment_text

	 return youtubevideo


 create_youtube_video("first review","nothing")


	
