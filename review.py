def create_youtube_video(title,description,hashtag) :
	newvideo = {"title" : title,"description" : description,"likes" : 0,"dislikes" : 0,"comments" : {}, "hashtag" : hashtag}
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

def similarity_to_video(youtubevideo1,youtubevideo2):
	num = len(youtubevideo1)
	similar = 0
	for i in range (num):
		if youtubevideo1[i] == youtubevideo2[i] :
			similar = similar +1

	return similar/num




n = create_youtube_video("first review","nothing",["amazing","wow","les go","nice","genuis"])
for i in range (494) :
	like(n)
print(n) 



	
