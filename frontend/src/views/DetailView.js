import React from 'react'
// import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag';

const INGREDIENT_QUERY = gql`
	query getIngredient($id: ID!){
		ingredient(id: $id) {
			id, name
		}
	}
`

class DetailView extends React.Component {
    render() {
    	let {data} = this.props;
    	if(data.loading || !data.ingredient) {
    		return <div>Loading...</div>
    	}
    	return (
    		<div>
    			<h1>Ingredient {data.ingredient.id}</h1>
    			<p>{data.ingredient.name}</p>
    		</div>
    	)
    }
}

const queryOptions = {
	options: (props) => ({
		variables: {
			id: props.match.params.id,
		},
	}),
}

DetailView = graphql(INGREDIENT_QUERY, queryOptions)(DetailView);

export default DetailView