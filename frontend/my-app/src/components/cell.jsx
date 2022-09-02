import React,{useState, useEffect} from "react"

/**
 * This function generates a cell of the spreadsheet
 * @param {the property Object} props 
 * @returns the html of a cell
 */
function Cell(props){
    const [value, setValue] = useState("")

    useEffect(()=>{
        setValue(props.value)
    },[props.value])
    
    return(
        <input className='cell' type="text" value = {value}  onChange = {(val)=>{setValue(val.target.value)}}/>
    )
}

export default Cell;