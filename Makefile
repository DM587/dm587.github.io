JEKYLL_VERSION=latest
TAG=dm587

install:
	gem update --system # upgrade RubyGems
	gem install jekyll bundler
	bundle install # all gems in Gemfile



update:
	bundle update jekyll
	bundle update
	#sudo certified-update

build:
	bundle exec jekyll build

publish:
	bundle exec jekyll build --trace -d /home/marco/public_html/Teaching/AY2024-2025/DM587
	#cp -fr _site/* /home/marco/public_html/Teaching/AY2024-2025/DM587/ 

serve: build
	bundle exec jekyll serve --watch

clean:
	rm -fr /home/marco/WWWpublic/DM561/*

show:
	bundle show minima


dockupdate:
	docker run --rm \
		--volume="${PWD}:/srv/jekyll" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle" \
		-it jekyll/jekyll:${JEKYLL_VERSION} \
		bundle update

dockbuild:
	docker run --rm \
		--volume="${PWD}:/srv/jekyll" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle" \
		-it jekyll/jekyll:${JEKYLL_VERSION} \
		jekyll build --trace



dockserve:
	docker run --rm \
		--volume="${PWD}:/srv/jekyll" \
		--volume="${PWD}/vendor/bundle:/usr/local/bundle" \
		-p 4000:4000 \
		-it jekyll/jekyll:${JEKYLL_VERSION} \
		jekyll serve --watch #--drafts
