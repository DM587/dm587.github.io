remote=../assets
# ${HOME}/WWWpublic/DM559/Resources/Ipython

%.html: %.ipynb
	jupyter nbconvert --to html --template full $<
	#cp $@ ${remote}

#%.html: %.ipynb
#	jupyter nbconvert --template basic $<
#	cp $@ ${remote}
