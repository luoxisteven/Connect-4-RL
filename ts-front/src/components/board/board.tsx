import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';


export default function BasicGrid() {
  return (
    <Box>
      <Grid container spacing={2}>
        <Grid size={4}>
            1
        </Grid>
        <Grid size={4}>
            2
        </Grid>
        <Grid size={4}>
            3
        </Grid>
        <Grid size={4}>
            4
        </Grid>
      </Grid>
    </Box>
  );
}