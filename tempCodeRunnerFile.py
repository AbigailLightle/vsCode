    # RECTANGLE (Law Of Gravitation)  
    pygame.draw.rect(SCREEN, Planet.GRAY, (30,640,290,220),
                     width = 0, border_radius = 20)
    pygame.draw.rect(SCREEN, Planet.WHITE, (30,640,290,220),
                     width = 3, border_radius = 20) 
    
    SCREEN.blit(text_gravity, (78,650))
    SCREEN.blit(img_newton, (35,685))
    SCREEN.blit(text_scaled, (55,872))