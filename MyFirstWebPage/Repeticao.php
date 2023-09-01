<?php
$var1=5;
$var2='5';

if ($var1 ==$var2){
    echo '$var1 e igual a $var2 \n\n';

}else{
    echo '$var1 nao e igual a var2\n\n';
}

endif;

echo "\n\nOperador Ternario \n\n";
$comparacao = (($var1===$var2)) ? "Iguais ou do mesmo tipo": "Apenas iguais";
echo $comparacao;
echo "\n\n"