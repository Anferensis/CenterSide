
/* Written by Albert"Anferensis"Ong
 * 
 * Revision: 07.16.2018
 */

import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.*;
import javax.swing.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class CenterSideGameWindow extends JFrame implements ActionListener {
	
	private JLabel background;
	private static Tile buttons[][] = new Tile[13][13];
	private static String current_color = "RED";
		

	public CenterSideGameWindow(String title) {
		
		super(title);
		
		//~ ImageIcon background_image = new ImageIcon("Image files/test_background.png"); 
		//~ background = new JLabel(background_image);
		//~ setBackground(background);
		
		setLayout(new GridLayout(13, 13, 2, 2));
		
		// Uses two for loops to generate a grid of Tile objects. 
		for (int x = 0; x < 13; x++) {
			for (int y = 0; y < 13; y++) {
				
				buttons[x][y] = new Tile();
				
				// Makes the center button blank. 
				if (x == 6 && y == 6) {
					buttons[x][y].setSelected(true);
					buttons[x][y].setOpaque(true);
					// buttons[x][y].setBorderPainted(false);
					buttons[x][y].setBackground(new Color(102, 102, 102));
				}
				else {
					buttons[x][y].addActionListener(this);
				}
					
				buttons[x][y].setXCoord(x);
				buttons[x][y].setYCoord(y);
				
				buttons[x][y].setContentAreaFilled(false);
				add(buttons[x][y]);
			}
		}
		
		buttons[6][6].setOpaque(true);
		buttons[6][6].setBackground(new Color(102, 102, 102));
		
		setSize(600, 600);
		setLocationRelativeTo(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);		
		setVisible(true);	
		
	}
	
	
	public void actionPerformed(ActionEvent event) {
		
		Tile button = (Tile)event.getSource();
		button.setContentAreaFilled(true);
		
		// Checks it the button is not selected. 
		boolean not_selected = !button.isSelected();
		
		// Retrieves the coordinate of the button. 
		ArrayList<Integer> button_coord = new ArrayList();
		
		// Fix this ineffecient algorithm later. 
		for (int x = 0; x < 13; x++) {
			for (int y = 0; y < 13; y++) {
				
				if (button == buttons[y][x]) {
					button_coord = new ArrayList(Arrays.asList(x, y));
				}
			}
		}
		
		boolean is_viable_coord = getViableCoords().contains(button_coord);
		
		if (not_selected && is_viable_coord) {
			
			String new_color_name;
			Color new_color_object;
			
			if (current_color == "RED") {
				new_color_object = new Color(171, 36, 36);
				new_color_name = "BLACK";
			}
			else {
				new_color_object = new Color(0, 0, 0);
				new_color_name = "RED";
			}
			
			button.setBackground(new_color_object);
			button.setColor(current_color);
			button.setSelected(true);
			
			System.out.println(current_color);
			current_color = new_color_name;
		}
	}
	
	public static ArrayList<ArrayList<Integer>> getViableCoords() {
		
		ArrayList<ArrayList<Integer>> viable_coords = new ArrayList();
		
		for (int x = 0; x < 13; x++) {
			for (int y = 0; y < 13; y++) {
				
				Tile tile = buttons[y][x];
				
				if (tile.isSelected()) {
					
					int[][] coord_changes = {{ 1,  0}, 
											 {-1,  0}, 
											 { 0,  1}, 
											 { 0, -1}};
					
					for (int[] coord_change : coord_changes) {
						
						int test_x = x + coord_change[0];
						int test_y = y + coord_change[1];
						
						boolean isViable = 0 <= test_x && test_x <= 12 
										&& 0 <= test_y && test_y <= 12;
										
						if (isViable) {
							Tile test_tile = buttons[test_y][test_x];
							
							if (!test_tile.isSelected()) {
								
								ArrayList<Integer> new_coord = new ArrayList(Arrays.asList(test_x, test_y));
								viable_coords.add(new_coord);
							}
						}
						
						
					}
				}
				
			}
		}
		
		return viable_coords;
	}
}


public class CenterSideGame {
	
  public static void main(String[] args) {

	CenterSideGameWindow test = new CenterSideGameWindow("Grid Buttons Testing");
	
	}
}

