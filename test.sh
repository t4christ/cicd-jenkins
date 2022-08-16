#!/bin/bash
# NOTE : Quote it else use array to avoid problems #
# FILES="/Users/macbookpro/Documents/t4cassets/logoandflyer/*.png"
# for f in $FILES
# do
# echo "Processing $f"
# #   mv $f /Users/macbookpro/Public/T4c/t4c/digital_cdn/assets/img/logo/logoflyer.png
# done

files="/Users/macbookpro/Documents/t4cassets/logoandflyer/*"


for file in /Users/macbookpro/Public/T4c/t4c/digital_cdn/assets/img/logo/*; do
    ext="${file##*.}"
    # echo "$ext"
    if [[ $ext == jpg ]]; then

        ((num++))
        # echo "$file /"
        mv "$file" "/Users/macbookpro/Public/T4c/t4c/digital_cdn/assets/img/portfolio/logoflyer$num.jpg"

        # mv "$f" "/Users/macbookpro/Public/T4c/t4c/digital_cdn/assets/img/logo"
    fi
done

