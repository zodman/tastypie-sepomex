for file in *.txt; do
        iconv -f ISO-8859-1 -t utf-8 "$file" -o "${file%.txt}.utf8.txt"

        rm "${file}"
done
