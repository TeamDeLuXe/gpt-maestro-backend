<?php
/*
Plugin Name: Mon Plugin Simple
Description: Plugin WordPress de base.
Version: 1.0
*/

add_shortcode('bonjour', function() {
    return 'Bonjour depuis mon plugin !';
});