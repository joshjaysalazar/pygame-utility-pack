import pygame


class RectOverlay:
    """A class for drawing rectangles around sprites.
    
    Args:
        sprite_groups (list, optional): A list of sprite groups to draw
            rectangles around (default None).
    """

    def __init__(self, sprite_groups=None):
        """Initializes the RectOverlay with the given Pygame screen.
        
        Args:
            sprite_groups (list, optional): A list of sprite groups to draw
                rectangles around (default None).
                
        Returns:
            None
        """

        # Member variables
        self.sprite_groups = sprite_groups

        # Screen variable
        self.screen = pygame.display.get_surface()

        # Flag indicating whether the RectOverlay is visible
        self.visible = True

        # Surface used to draw the RectOverlay, set to the size of the screen
        self.overlay_surface = pygame.Surface(
            pygame.display.get_surface().get_size(),
            pygame.SRCALPHA
        )

    def toggle_visible(self, enabled=None):
        """Toggles the visibility of the DebugOverlay.

        Args:
            enabled (bool, optional): Whether to enable the overlay 
                (default None).

        Returns:
            None
        """

        # Toggle the visibility if enabled is None, or set it to the given value
        if enabled is None:
            self.visible = not self.visible
        else:
            self.visible = enabled

    def add_sprite_group(self, sprite_group):
        """Adds a sprite group to the RectOverlay.

        Args:
            sprite_group (pygame.sprite.Group): The sprite group to add.

        Returns:
            None
        """

        # Add the sprite group to the list of sprite groups
        self.sprite_groups.append(sprite_group)

    def remove_sprite_group(self, sprite_group):
        """Removes a sprite group from the RectOverlay.

        Args:
            sprite_group (pygame.sprite.Group): The sprite group to remove.

        Returns:
            None
        """

        # Remove the sprite group from the list of sprite groups
        self.sprite_groups.remove(sprite_group)

    def draw(self, normal_color="green", collision_color="red", rect_width=1):
        """Draws the RectOverlay on the screen.

        This method clears the overlay surface, and then iterates through each
        sprite in the sprite groups. It checks for collisions between the sprite
        and other sprites in the groups. If a collision is detected, a red
        rectangle is drawn around the sprite; otherwise, a green rectangle is
        drawn. Finally, the overlay surface is drawn on the screen.

        Args:
            normal_color (str, optional): The color to use for non-
                    colliding sprites (default "green").
            collision_color (str, optional): The color to use for colliding
                sprites (default "red").
            rect_width (int, optional): The width of the rectangles to draw
                (default 1).

        Returns:
            None
        """

        # Clear the overlay surface
        self.overlay_surface.fill((0, 0, 0, 0))

        # Loop through each sprite in each sprite group
        for sprite_group in self.sprite_groups:
            for sprite in sprite_group:

                # Initialize the colliding flag as False
                colliding = False

                # Loop through each group to check for collisions
                for group in self.sprite_groups:
                    collisions = pygame.sprite.spritecollide(
                        sprite,
                        group,
                        False
                    )

                    # Loop through the collisions
                    for collision in collisions: 
                        if collision != sprite:
                            colliding = True
                            break

                    # If the colliding flag is True, break the outer loop
                    if colliding:
                        break

                # If the sprite is colliding, draw a red rectangle around it
                if colliding:
                    pygame.draw.rect(
                        self.overlay_surface,
                        collision_color,
                        sprite.rect,
                        rect_width
                    )
                # If the sprite is not colliding, draw a green rectangle
                else:
                    pygame.draw.rect(
                        self.overlay_surface,
                        normal_color,
                        sprite.rect,
                        rect_width
                    )

        # Draw the overlay surface to the screen
        self.screen.blit(self.overlay_surface, (0, 0))
