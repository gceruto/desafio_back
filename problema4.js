
function isAnagram(text1, text2)
{    
    t1 = [...text1].sort().toString();
    t2 = [...text2].sort().toString();

    return t1 == t2;
}
