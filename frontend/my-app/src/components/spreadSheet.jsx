import React, {useState, useEffect} from "react"
import "./spreadsheet.css"
import Cell from "./cell"

/**
 * The spreadsheet component function
 * @return thr spreadsheet in html
 */
function SpreadSheet(props){
    var emptySheet = Array(200).fill().map(() => Array(26).fill(""))
    const header = [...Array(27).keys()]
    const[spreadsheet, setspreadsheet] = useState(emptySheet)
    const [python, setPython] = useState("")
    var data = props.data
    var sheet = props.sheet
    
    const err = "invalid parameter"

    
    useEffect(()=>{
        handle()
    },[JSON.stringify(props.data), JSON.stringify(sheet)])

    useEffect(()=>{
        if(props.sheet != "") {
            props.passPy(python)
        }
    },[python])

    for(var row = 0; row < data.length; row++) {
        for(var col = 0; col < data[row].length; col++) {
            emptySheet[row][col] = data[row][col]
        }
    }   

    const handle=()=>{
        if(data == {} ){
            console.log(err);
        } else {
            var dataset = data[sheet]
            if(dataset == undefined){
                console.log(err)
            } else {
                for(var row = 0; row < dataset.length; row++) {
                    for(var col = 0; col < dataset[row].length; col++){
                        emptySheet[row][col] = dataset[row][col]
                    }
                }
                setspreadsheet(emptySheet)
            }
        }
    }

    return(
        <div>
            <div className = "sheets">
                <table>
                    <tr>
                        {header.map((e)=>{
                            return <th>{e}</th>
                        })}
                    </tr>
                    {spreadsheet.map((item, index)=>{
                        item = [index+1].concat(item)
                        return <tr>
                            {item.map((element, position)=>{
                                return <td id = {index+1 + "," + position }>  
                                            <Cell  location = {[index+1,position]} sheet = {sheet}  value = {element} sheetName = {sheet} pyChange = {(code)=>{setPython(code)}}/> 
                                        </td>
                            })}
                        </tr>
                    })}
                </table>
            </div>
        </div>
    )
}

export default SpreadSheet;