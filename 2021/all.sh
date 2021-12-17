for i in $(seq -f "%02g" 1 25)
do
    echo
    echo "### Challenge day $i"
    python $i.py
    echo
done

