for i in {0..391..1}
do
    if [ -f ./allxmls/$i/build.xml ]; then
        echo "Taking care of build $i"
        python parse_build.py ./allxmls/$i/build.xml m730_android $i
        sleep 1
    fi
done
