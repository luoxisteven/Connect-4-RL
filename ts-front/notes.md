# React Learning

# Import and Display
``` tsx
import BasicGrid from "./components/board/board";

export default function Game() {
  return (
    // <BasicGrid></BasicGrid>
    <BasicGrid />
  );
}

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';


export default function BasicGrid() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid container spacing={2}>
        <Grid size={8}>
            1
        </Grid>
        <Grid size={4}>
            2
        </Grid>
        <Grid size={4}>
            3
        </Grid>
        <Grid size={8}>
            4
        </Grid>
      </Grid>
    </Box>
  );
}
```