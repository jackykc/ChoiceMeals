import React from 'react'
import { Link } from 'react-router-dom'
import { graphql } from 'react-apollo'
import gql from 'graphql-tag';

const INGREDIENTS_QUERY = gql`
query {
  allIngredients {
    id
    name
  }
}
`;

class ListView extends React.Component {

    render() {
    	let {data} = this.props
    	if (data.loading || !data.allIngredients) {
      		return <div>Loading...</div>
    	}
      
    	return (
    		<div>
    			{data.allIngredients.map(item=> (
    				<p key={item.id}>
    					<Link to={`/ingredient/${item.id}/`}>
    						{item.name}
    					</Link>
    				</p>
				))}
			</div>
    	)
    }
}

ListView = graphql(INGREDIENTS_QUERY)(ListView)

export default ListView