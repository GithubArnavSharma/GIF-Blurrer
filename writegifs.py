#Using the blur_gif function, we can now convert gifs from non-blurred to blurred
#See results of this code in the 'results' folder

#The first gif converted is a simple gif of someone from far away walking. The fps will be 15 to make it smooth
blur_gif('walking.gif', 'blurred_walking.gif', fps=15)
#The second gif is a gif of multiple people in an audience laughing. The fps will be 15 to make it smooth
blur_gif('laughing.gif', 'blurred_laughing.gif', fps=15)
#The third gif is a short gif of two people, with one of them putting a thumbs up. Since the total frames is 10, the fps will be 10
blur_gif('thumbsup.gif', 'blurred_thumbsup.gif', fps=10)
#The fourth gif is a clip from last of us with people in an audience. The fps will be 12 to make it smooth but not too fast
blur_gif('lastofus.gif', 'blurred_lastofus.gif', fps=12)
