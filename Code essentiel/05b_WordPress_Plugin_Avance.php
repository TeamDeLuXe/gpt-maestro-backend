<?php
/*
Plugin Name: Gestionnaire Avancé de Contenu
Description: Un plugin WordPress avancé avec page d'options, CPT, shortcode et REST API.
Version: 1.0
Author: TeamDeLuxe
*/

// Création d'un Custom Post Type
function gpt_register_custom_post_type() {
    register_post_type('ressource', array(
        'labels' => array(
            'name' => 'Ressources',
            'singular_name' => 'Ressource'
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'custom-fields')
    ));
}
add_action('init', 'gpt_register_custom_post_type');

// Shortcode simple
function gpt_affiche_ressources() {
    $posts = get_posts(array('post_type' => 'ressource', 'numberposts' => 5));
    $output = '<ul>';
    foreach ($posts as $post) {
        $output .= '<li>' . esc_html($post->post_title) . '</li>';
    }
    $output .= '</ul>';
    return $output;
}
add_shortcode('liste_ressources', 'gpt_affiche_ressources');

// Ajout d'une route REST API
add_action('rest_api_init', function () {
    register_rest_route('gpt-maestro/v1', '/ressources/', array(
        'methods' => 'GET',
        'callback' => 'gpt_api_get_ressources',
    ));
});
function gpt_api_get_ressources() {
    $posts = get_posts(array('post_type' => 'ressource', 'numberposts' => 5));
    $data = array();
    foreach ($posts as $post) {
        $data[] = array('id' => $post->ID, 'title' => $post->post_title);
    }
    return rest_ensure_response($data);
}
