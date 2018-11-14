for i in $(seq 100)
do
    git commit --allow-empty -m "[CI] fix, try n° $i"
    git push origin quentinMondon
done
