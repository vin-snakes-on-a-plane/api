import React from 'react'
import axios from "axios";
import './Plane.css'

const API_URL_SETTINGS = 'http://127.0.0.1:8000/api/gameboard'

class Plane extends React.Component {

    constructor(props) {

        super(props);

        this.state = {
            player: {
                x_pos: 4,
                y_pos: 3,
            },
            rows: []
        }

        console.log('construct')
    }

   /**
    *
    */
   componentDidMount() {
      this.loadSettings();
   }

/**
    *
    */
   loadSettings() {

       console.log('loadSettings()')

      // **** Always work with a copy of STATE
      let curstat = this.state;

      // *** Make REST call
      axios
         .get(API_URL_SETTINGS)
         .then(response => {

            console.log(response.data)

            if (Array.isArray(response.data)) {

            //    // *** Work with a copy of STATE
            //    let change = this.state;

            //    // *** Loop through returned NVPs
            //    response.data.forEach(function(restobj) {
            //       if (typeof restobj.value !== 'undefined') {
            //          change[restobj.name] = restobj.value;
            //       }
            //       else
            //          console.log('loadSettings()::Value Not Returned from REST::name:', restobj.name);
            //    })

            //    // *** Blast out the new STATE
            //    this.setState(change);

            //    // *** Update UI
            //    this.uiSet(change);

            } else {
               console.log("ERROR: response.data is not an array");
            }

         })
         .catch(error => console.log(error));
   }

    /**
     * API data like this
     * [{x_pos:0,y_pos:0}....] all in one array (order gauranteed????)
     * We want ideally in nested arrays
     */
    renderRows() {

        const rowsToRender = []

        for (let row of this.state.rows) {

            let cellsToRender = row.map(cell => {

                let className = 'Cell ' + cell.cell_type;

                if (cell.x_pos === this.state.player.x_pos &&
                    cell.y_pos === this.state.player.y_pos) {
                        className += ' player'
                    }


                return <div className={className}>{cell.cell_type}</div>
            })

            rowsToRender.push(cellsToRender);

        }

        return rowsToRender;
    }




    render() {
        return (<div className="Plane">
            {this.renderRows()}
        </div>)
    }
}

export default Plane