# puppet codee that fixes 500 error on a wordpress site
# editing the misspelled "phpp" to php
exec { 'fix-wordpress':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/:/usr/loca/bin/',
}
