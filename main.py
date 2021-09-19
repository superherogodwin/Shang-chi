@namespace
class SpriteKind:
    Ring = SpriteKind.create()

def on_on_created(sprite):
    animation.loop_frames2(sprite,
        assets.animation("""
            assassin left
        """),
        125,
        characterAnimations.rule(Predicate.MOVING_LEFT))
    sprite.follow(mySprite, 30)
    sprite.ay = 500
    animation.loop_frames2(sprite,
        assets.animation("""
            assassin right
        """),
        125,
        characterAnimations.rule(Predicate.MOVING_RIGHT))
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_up_pressed():
    sprites.gravity_jump(mySprite)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite2, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        pit
    """),
    on_overlap_tile)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        power kick
    """), mySprite, 50, 50)
    projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    projectile.lifespan = 100
    animation.run_image_animation(mySprite, assets.animation("""
        sc kick
    """), 125, False)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    tiles.set_wall_at(tiles.location_in_direction(tiles.location_of_sprite(mySprite),
            CollisionDirection.BOTTOM),
        True)
    tiles.set_tile_at(tiles.location_in_direction(tiles.location_of_sprite(mySprite),
            CollisionDirection.BOTTOM),
        assets.tile("""
            energy
        """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_hit_wall(sprite3, location2):
    sprites.wall_jump(sprite3)
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

def on_overlap_tile2(sprite4, location3):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        door2
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite5, location4):
    tiles.set_tile_at(location4, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        ring
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite6, location5):
    tiles.set_wall_at(location5, False)
    tiles.set_tile_at(location5, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        boulder
    """),
    on_overlap_tile4)

def on_on_overlap(sprite7, otherSprite):
    otherSprite.destroy()
    sprite7.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_overlap_tile5(sprite8, location6):
    scene.set_background_image(assets.image("""
        background2
    """))
    tiles.set_tilemap(tilemap("""
        level2
    """))
    animation.run_movement_animation(mySprite,
        animation.animation_presets(animation.fly_to_center),
        2000,
        False)
    game.level_num(2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        door1
    """),
    on_overlap_tile5)

def on_on_overlap2(sprite9, otherSprite2):
    tiles.place_on_random_tile(otherSprite2, assets.tile("""
        rubble
    """))
    info.change_life_by(-1)
    animation.run_image_animation(mySprite,
        assets.animation("""
            sc damage
        """),
        200,
        False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    background1
"""))
tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(assets.image("""
    Shang-Chi
"""), SpriteKind.player)
sprites.add_profile(Choice.SHANG)
mySprite.ay = 500
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite, 100, 0)
animation.loop_frames2(mySprite,
    assets.animation("""
        sc walk right
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_RIGHT))
animation.loop_frames2(mySprite,
    assets.animation("""
        sc walk left
    """),
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT))
animation.loop_frames2(mySprite,
    assets.animation("""
        sc jump
    """),
    125,
    characterAnimations.rule(Predicate.MOVING_UP))
tiles.create_sprites_on_tiles(assets.tile("""
    rubble
"""), SpriteKind.enemy)