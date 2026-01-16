export default function Square({value, onSquareClick} : {value: string, onSquareClick:()=> void}) {
    return(
    <button onClick={onSquareClick}>
        {value}
    </button>
    )
}

function onSquareClick(){
    return
}